import FWCore.ParameterSet.Config as cms

def L1ExtraDQM(**kwargs):
  mod = cms.EDProducer('L1ExtraDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod