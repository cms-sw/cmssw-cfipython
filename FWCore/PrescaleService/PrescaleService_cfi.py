import FWCore.ParameterSet.Config as cms

PrescaleService = cms.Service('PrescaleService',
  lvl1Labels = cms.vstring('default'),
  prescaleTable = cms.VPSet(
    cms.PSet(
      pathName = cms.string('HLTPath'),
      prescales = cms.vuint32(1)
    )
  ),
  lvl1DefaultLabel = cms.string('default'),
  forceDefault = cms.bool(False)
)
