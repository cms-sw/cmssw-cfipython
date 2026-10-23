import FWCore.ParameterSet.Config as cms

def JetTester(*args, **kwargs):
  mod = cms.EDProducer('JetTester',
    isHLT = cms.untracked.bool(False),
    JetType = cms.untracked.string('pf'),
    src = cms.InputTag('ak4PFJets'),
    srcGen = cms.InputTag('ak4GenJetsNoNu'),
    JetCorrections = cms.InputTag('newAk4PFL1FastL2L3Corrector'),
    primVertex = cms.InputTag('offlinePrimaryVertices'),
    recoJetPtThreshold = cms.double(40),
    matchGenPtThreshold = cms.double(20),
    RThreshold = cms.double(0.3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
