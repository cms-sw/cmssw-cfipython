import FWCore.ParameterSet.Config as cms

def EgammaHLTFilteredEcalCandPtrProducer(**kwargs):
  mod = cms.EDProducer('EgammaHLTFilteredEcalCandPtrProducer',
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
