import FWCore.ParameterSet.Config as cms

def FFTBasicJetSysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTBasicJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
