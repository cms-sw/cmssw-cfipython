import FWCore.ParameterSet.Config as cms

def FFTPF2CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
