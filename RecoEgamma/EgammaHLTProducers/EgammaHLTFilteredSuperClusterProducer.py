import FWCore.ParameterSet.Config as cms

def EgammaHLTFilteredSuperClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTFilteredSuperClusterProducer',
    cands = cms.InputTag('hltEgammaCandidates'),
    minEtCutEB = cms.double(0),
    minEtCutEE = cms.double(0),
    cuts = cms.VPSet(
      cms.PSet(
        var = cms.InputTag('hltEgammaHoverE'),
        barrelCut = cms.PSet(
          cutOverE = cms.double(0.2),
          doAnd = cms.double(0),
          useEt = cms.double(0)
        ),
        endcapCut = cms.PSet(
          cutOverE = cms.double(0.2),
          doAnd = cms.double(0),
          useEt = cms.double(0)
        )
      ),
      template = cms.PSetTemplate(
        barrelCut = cms.PSet(
          cut = cms.double(-1),
          cutOverE = cms.double(-1),
          cutOverE2 = cms.double(-1),
          useEt = cms.bool(False),
          doAnd = cms.bool(False)
        ),
        endcapCut = cms.PSet(
          cut = cms.double(-1),
          cutOverE = cms.double(-1),
          cutOverE2 = cms.double(-1),
          useEt = cms.bool(False),
          doAnd = cms.bool(False)
        ),
        var = cms.InputTag('hltEgammaHoverE')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
