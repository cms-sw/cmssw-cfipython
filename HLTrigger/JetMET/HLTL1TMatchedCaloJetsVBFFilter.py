import FWCore.ParameterSet.Config as cms

def HLTL1TMatchedCaloJetsVBFFilter(**kwargs):
  mod = cms.EDFilter('HLTL1TMatchedCaloJetsVBFFilter',
    saveTags = cms.bool(True),
    src = cms.InputTag('hltJets'),
    matchJetsByDeltaR = cms.bool(True),
    maxJetDeltaR = cms.double(0.5),
    l1tJetRefs = cms.InputTag('hltL1sJetSeed'),
    algorithm = cms.string('VBF'),
    minPt1 = cms.double(110),
    minPt2 = cms.double(35),
    minPt3 = cms.double(110),
    minInvMass = cms.double(650),
    minNJets = cms.int32(0),
    maxNJets = cms.int32(-1),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
