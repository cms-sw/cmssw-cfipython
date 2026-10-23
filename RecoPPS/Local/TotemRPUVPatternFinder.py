import FWCore.ParameterSet.Config as cms

def TotemRPUVPatternFinder(*args, **kwargs):
  mod = cms.EDProducer('TotemRPUVPatternFinder',
    tagRecHit = cms.InputTag('totemRPRecHitProducer'),
    verbosity = cms.untracked.uint32(0),
    maxHitsPerPlaneToSearch = cms.uint32(5),
    minPlanesPerProjectionToSearch = cms.uint32(3),
    clusterSize_a = cms.double(0.02),
    clusterSize_b = cms.double(0.3),
    threshold = cms.double(2.99),
    minPlanesPerProjectionToFit = cms.uint32(3),
    allowAmbiguousCombination = cms.bool(False),
    max_a_toFit = cms.double(10),
    exceptionalSettings = cms.VPSet(
      template = cms.PSetTemplate(
        rpId = cms.required.uint32,
        minPlanesPerProjectionToFit_U = cms.required.uint32,
        minPlanesPerProjectionToFit_V = cms.required.uint32,
        threshold_U = cms.required.double,
        threshold_V = cms.required.double
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
