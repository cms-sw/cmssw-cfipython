import FWCore.ParameterSet.Config as cms

def EcalEBTrigPrimPhase2Producer(*args, **kwargs):
  mod = cms.EDProducer('EcalEBTrigPrimPhase2Producer',
    Debug = cms.bool(False),
    binOfMaximum = cms.int32(6),
    barrelEcalDigis = cms.InputTag('simEcalUnsuppressedDigis'),
    spikeTagger = cms.PSet(
      algoType = cms.string('ld'),
      version = cms.uint32(1)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
