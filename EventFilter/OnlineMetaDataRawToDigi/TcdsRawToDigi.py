import FWCore.ParameterSet.Config as cms

def TcdsRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('TcdsRawToDigi',
    InputLabel = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
