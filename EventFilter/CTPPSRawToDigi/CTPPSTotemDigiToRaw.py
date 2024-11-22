import FWCore.ParameterSet.Config as cms

def CTPPSTotemDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('CTPPSTotemDigiToRaw',
    InputLabel = cms.InputTag('RPSiDetDigitizer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
