import FWCore.ParameterSet.Config as cms

def L1TEfficiencyHarvesting(**kwargs):
  mod = cms.EDProducer('L1TEfficiencyHarvesting',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod