import FWCore.ParameterSet.Config as cms

def EcalTBTDCRawInfoDumper(**kwargs):
  mod = cms.EDAnalyzer('EcalTBTDCRawInfoDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
