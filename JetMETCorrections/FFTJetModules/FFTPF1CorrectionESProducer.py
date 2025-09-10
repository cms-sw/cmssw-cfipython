import FWCore.ParameterSet.Config as cms

def FFTPF1CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
