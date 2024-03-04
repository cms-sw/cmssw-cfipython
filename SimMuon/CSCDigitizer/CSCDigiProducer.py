import FWCore.ParameterSet.Config as cms

def CSCDigiProducer(**kwargs):
  mod = cms.EDProducer('CSCDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
