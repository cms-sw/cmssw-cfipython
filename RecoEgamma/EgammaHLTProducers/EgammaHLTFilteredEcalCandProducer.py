import FWCore.ParameterSet.Config as cms

def EgammaHLTFilteredEcalCandProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTFilteredEcalCandProducer',
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
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
