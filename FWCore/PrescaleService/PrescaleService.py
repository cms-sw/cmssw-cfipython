import FWCore.ParameterSet.Config as cms

def PrescaleService(*args, **kwargs):
  mod = cms.Service('PrescaleService',
    lvl1Labels = cms.vstring('default'),
    prescaleTable = cms.VPSet(
      cms.PSet(
        pathName = cms.string('HLTPath'),
        prescales = cms.vuint32(1)
      ),
      template = cms.PSetTemplate(
        pathName = cms.required.string,
        prescales = cms.required.vuint32
      )
    ),
    lvl1DefaultLabel = cms.string('default'),
    forceDefault = cms.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
