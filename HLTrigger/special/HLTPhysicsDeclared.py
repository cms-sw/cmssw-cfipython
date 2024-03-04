import FWCore.ParameterSet.Config as cms

def HLTPhysicsDeclared(**kwargs):
  mod = cms.EDFilter('HLTPhysicsDeclared',
    L1GtReadoutRecordTag = cms.InputTag('hltGtDigis'),
    invert = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
