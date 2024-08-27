import FWCore.ParameterSet.Config as cms

def ConversionColMerger(**kwargs):
  mod = cms.EDProducer('ConversionColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
