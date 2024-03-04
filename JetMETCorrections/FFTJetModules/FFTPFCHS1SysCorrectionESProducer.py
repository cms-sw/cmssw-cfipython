import FWCore.ParameterSet.Config as cms

def FFTPFCHS1SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFCHS1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
