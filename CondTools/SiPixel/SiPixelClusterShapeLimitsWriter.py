import FWCore.ParameterSet.Config as cms

def SiPixelClusterShapeLimitsWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelClusterShapeLimitsWriter',
    tables = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.required.string,
        file = cms.required.FileInPath
      )
    ),
    rules = cms.VPSet(
      template = cms.PSetTemplate(
        subdet = cms.required.string,
        layerOrDisk = cms.int32(0),
        table = cms.required.string
      )
    ),
    record = cms.string('SiPixelClusterShapeLimitsRcd'),
    printDebug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
