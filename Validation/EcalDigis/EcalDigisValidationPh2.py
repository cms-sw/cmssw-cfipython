import FWCore.ParameterSet.Config as cms

def EcalDigisValidationPh2(*args, **kwargs):
  mod = cms.EDProducer('EcalDigisValidationPh2',
    digiCollection = cms.InputTag('simEcalUnsuppressedDigis'),
    moduleLabelMC = cms.string('generatorSmeared'),
    moduleLabelG4 = cms.string('g4SimHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
