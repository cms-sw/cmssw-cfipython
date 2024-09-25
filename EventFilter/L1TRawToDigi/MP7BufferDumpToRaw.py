import FWCore.ParameterSet.Config as cms

def MP7BufferDumpToRaw(*args, **kwargs):
  mod = cms.EDProducer('MP7BufferDumpToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
