import FWCore.ParameterSet.Config as cms

def FFTPF0CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF0CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
