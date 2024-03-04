import FWCore.ParameterSet.Config as cms

def HLTFatPFJetMassFilter(**kwargs):
  mod = cms.EDFilter('HLTFatPFJetMassFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('hltCollection'),
    minMass = cms.double(0),
    fatJetDeltaR = cms.double(1.1),
    maxDeltaEta = cms.double(10),
    maxJetEta = cms.double(3),
    minJetPt = cms.double(30),
    triggerType = cms.int32(85),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
