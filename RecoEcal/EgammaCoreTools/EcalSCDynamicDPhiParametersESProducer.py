import FWCore.ParameterSet.Config as cms

def EcalSCDynamicDPhiParametersESProducer(**kwargs):
  mod = cms.ESProducer('EcalSCDynamicDPhiParametersESProducer',
    dynamicDPhiParameterSets = cms.VPSet(
      cms.PSet(
        cutoff = cms.double(0.6),
        eMin = cms.double(0),
        etaMin = cms.double(0),
        saturation = cms.double(0.14),
        scale = cms.double(0.946048),
        width = cms.double(0.432767),
        xoffset = cms.double(-0.101172),
        yoffset = cms.double(0.0280506)
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
