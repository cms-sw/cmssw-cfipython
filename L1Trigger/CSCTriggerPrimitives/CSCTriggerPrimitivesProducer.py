import FWCore.ParameterSet.Config as cms

def CSCTriggerPrimitivesProducer(**kwargs):
  mod = cms.EDProducer('CSCTriggerPrimitivesProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
