import FWCore.ParameterSet.Config as cms

def CSCTnPEfficiencyTask(**kwargs):
  mod = cms.EDProducer('CSCTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
