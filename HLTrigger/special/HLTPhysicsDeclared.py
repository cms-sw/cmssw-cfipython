import FWCore.ParameterSet.Config as cms

def HLTPhysicsDeclared(*args, **kwargs):
  mod = cms.EDFilter('HLTPhysicsDeclared',
    L1GtReadoutRecordTag = cms.InputTag('hltGtDigis'),
    invert = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
