import FWCore.ParameterSet.Config as cms

def TestWriteL1Scouting(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
