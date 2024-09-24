import FWCore.ParameterSet.Config as cms

def FFTPFCHS0SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFCHS0SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod