import FWCore.ParameterSet.Config as cms

def CTPPSTotemDigiToRaw(**kwargs):
  mod = cms.EDProducer('CTPPSTotemDigiToRaw',
    InputLabel = cms.InputTag('RPSiDetDigitizer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
