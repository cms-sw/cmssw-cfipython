import FWCore.ParameterSet.Config as cms

def PrimaryVertexObjectFilter(*args, **kwargs):
  mod = cms.EDFilter('PrimaryVertexObjectFilter',
    src = cms.InputTag(''),
    filterParams = cms.PSet(
      minNdof = cms.double(4),
      maxZ = cms.double(24),
      maxRho = cms.double(2),
      cutsToIgnore = cms.vstring()
    ),
    filter = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
