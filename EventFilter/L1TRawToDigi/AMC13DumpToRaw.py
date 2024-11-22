import FWCore.ParameterSet.Config as cms

def AMC13DumpToRaw(*args, **kwargs):
  mod = cms.EDProducer('AMC13DumpToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
