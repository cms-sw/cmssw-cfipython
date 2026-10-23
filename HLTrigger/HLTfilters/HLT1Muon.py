import FWCore.ParameterSet.Config as cms

def HLT1Muon(*args, **kwargs):
  mod = cms.EDFilter('HLT1Muon',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltCollection'),
    triggerType = cms.int32(0),
    MinE = cms.double(-1),
    MinPt = cms.double(-1),
    MinMass = cms.double(-1),
    MaxMass = cms.double(-1),
    MinEta = cms.double(-1),
    MaxEta = cms.double(-1),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
