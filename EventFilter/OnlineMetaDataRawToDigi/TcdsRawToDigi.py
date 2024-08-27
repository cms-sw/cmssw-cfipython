import FWCore.ParameterSet.Config as cms

def TcdsRawToDigi(**kwargs):
  mod = cms.EDProducer('TcdsRawToDigi',
    InputLabel = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
