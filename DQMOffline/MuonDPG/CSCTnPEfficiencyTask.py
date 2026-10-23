import FWCore.ParameterSet.Config as cms

def CSCTnPEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('CSCTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
