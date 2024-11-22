import FWCore.ParameterSet.Config as cms

def LeptonTaggerByIPESProducer(*args, **kwargs):
  mod = cms.ESProducer('LeptonTaggerByIPESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
