import FWCore.ParameterSet.Config as cms

def EcalTBTDCRawInfoDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTBTDCRawInfoDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
