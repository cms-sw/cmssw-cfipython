import FWCore.ParameterSet.Config as cms

def PrimaryVertexFilter(*args, **kwargs):
  mod = cms.EDFilter('PrimaryVertexFilter',
    minNdof = cms.double(4),
    maxZ = cms.double(24),
    maxRho = cms.double(2),
    cutsToIgnore = cms.vstring(),
    pvSrc = cms.InputTag(''),
    NPV = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
