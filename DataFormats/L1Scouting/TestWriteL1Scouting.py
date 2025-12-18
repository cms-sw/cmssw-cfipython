import FWCore.ParameterSet.Config as cms

def TestWriteL1Scouting(*args, **kwargs):
  mod = cms.EDProducer('TestWriteL1Scouting',
    bxValues = cms.required.vuint32,
    muonValues = cms.required.vint32,
    jetValues = cms.required.vint32,
    eGammaValues = cms.required.vint32,
    tauValues = cms.required.vint32,
    bxSumsValues = cms.required.vint32,
    bmtfStubValues = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
