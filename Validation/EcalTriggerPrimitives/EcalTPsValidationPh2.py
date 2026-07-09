import FWCore.ParameterSet.Config as cms

def EcalTPsValidationPh2(*args, **kwargs):
  mod = cms.EDProducer('EcalTPsValidationPh2',
    tpDigiCollection = cms.InputTag('simEcalEBTriggerPrimitivePhase2Digis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
