import FWCore.ParameterSet.Config as cms

def AMC13DumpToRaw(**kwargs):
  mod = cms.EDProducer('AMC13DumpToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
