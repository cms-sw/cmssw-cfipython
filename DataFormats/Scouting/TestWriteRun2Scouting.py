import FWCore.ParameterSet.Config as cms

def TestWriteRun2Scouting(*args, **kwargs):
  mod = cms.EDProducer('TestWriteRun2Scouting',
    caloJetsValues = cms.required.vdouble,
    electronsFloatingPointValues = cms.required.vdouble,
    electronsIntegralValues = cms.required.vint32,
    muonsFloatingPointValues = cms.required.vdouble,
    muonsIntegralValues = cms.required.vint32,
    particlesFloatingPointValues = cms.required.vdouble,
    particlesIntegralValues = cms.required.vint32,
    pfJetsFloatingPointValues = cms.required.vdouble,
    pfJetsIntegralValues = cms.required.vint32,
    photonsFloatingPointValues = cms.required.vdouble,
    tracksFloatingPointValues = cms.required.vdouble,
    tracksIntegralValues = cms.required.vint32,
    vertexesFloatingPointValues = cms.required.vdouble,
    vertexesIntegralValues = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
