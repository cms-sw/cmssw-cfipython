import FWCore.ParameterSet.Config as cms

def CSCGeometryESModule(**kwargs):
  mod = cms.ESProducer('CSCGeometryESModule',
    fromDDD = cms.bool(True),
    fromDD4hep = cms.bool(False),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    useRealWireGeometry = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
