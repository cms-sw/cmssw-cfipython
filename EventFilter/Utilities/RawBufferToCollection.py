import FWCore.ParameterSet.Config as cms

def RawBufferToCollection(*args, **kwargs):
  mod = cms.EDProducer('RawBufferToCollection',
    source = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
