import FWCore.ParameterSet.Config as cms

def SiPhase2RecHitMatcherESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPhase2RecHitMatcherESProducer',
    offlinestubs = cms.string('vectorHits'),
    maxVectorHits = cms.int32(999999999),
    Algorithm = cms.string('VectorHitBuilderAlgorithm'),
    ComponentName = cms.string('SiPhase2VectorHitMatcher'),
    CPE = cms.ESInputTag('', 'Phase2StripCPE'),
    BarrelCut = cms.vdouble(
      0,
      0.05,
      0.06,
      0.08,
      0.09,
      0.12,
      0.2
    ),
    Phase2CPE_name = cms.string('Phase2StripCPE'),
    Clusters = cms.string('siPhase2Clusters'),
    maxVectorHitsInAStack = cms.int32(999),
    EndcapCut = cms.vdouble(
      0,
      0.1,
      0.1,
      0.1,
      0.1,
      0.1
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
