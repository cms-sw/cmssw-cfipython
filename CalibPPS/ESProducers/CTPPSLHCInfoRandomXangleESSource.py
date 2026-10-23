import FWCore.ParameterSet.Config as cms

def CTPPSLHCInfoRandomXangleESSource(*args, **kwargs):
  mod = cms.ESSource('CTPPSLHCInfoRandomXangleESSource',
    label = cms.string(''),
    seed = cms.uint32(1),
    generateEveryNEvents = cms.uint32(1),
    xangleBetaStarHistogramFile = cms.string(''),
    xangleBetaStarHistogramObject = cms.string(''),
    beamEnergy = cms.double(0),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
