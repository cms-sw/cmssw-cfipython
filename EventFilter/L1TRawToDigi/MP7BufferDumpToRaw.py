import FWCore.ParameterSet.Config as cms

def MP7BufferDumpToRaw(**kwargs):
  mod = cms.EDProducer('MP7BufferDumpToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
