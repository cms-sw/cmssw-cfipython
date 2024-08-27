import FWCore.ParameterSet.Config as cms

def FFTPFCHS2SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFCHS2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
