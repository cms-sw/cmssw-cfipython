import FWCore.ParameterSet.Config as cms

egammaHLTFilteredSuperClusterProducer = cms.EDProducer('EgammaHLTFilteredSuperClusterProducer',
  cands = cms.InputTag('hltEgammaCandidates'),
  minEtCutEB = cms.double(0),
  minEtCutEE = cms.double(0),
  cuts = cms.VPSet(
    cms.PSet(
      var = cms.InputTag('hltEgammaHoverE'),
      barrelCut = cms.PSet(
        cutOverE = cms.double(0.2),
        useEt = cms.double(0)
      ),
      endcapCut = cms.PSet(
        cutOverE = cms.double(0.2),
        useEt = cms.double(0)
      )
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
