import FWCore.ParameterSet.Config as cms

def HLTVertexTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTVertexTableProducer',
    skipNonExistingSrc = cms.bool(False),
    usePF = cms.bool(True),
    doSVs = cms.bool(True),
    pvName = cms.string('hltPrimaryVertex'),
    pvSrc = cms.InputTag('hltOfflinePrimaryVertices'),
    pfSrc = cms.InputTag('hltParticleFlowTmp'),
    goodPvCut = cms.string(''),
    svName = cms.string('hltSecondaryVertex'),
    svDoc = cms.string('secondary vertices from IVF algorithm'),
    svSrc = cms.InputTag('hltDeepInclusiveSecondaryVerticesPF'),
    goodSvCut = cms.string(''),
    dlenMin = cms.double(0),
    dlenSigMin = cms.double(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
