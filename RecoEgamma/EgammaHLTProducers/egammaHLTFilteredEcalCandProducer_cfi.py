import FWCore.ParameterSet.Config as cms

egammaHLTFilteredEcalCandProducer = cms.EDProducer('EgammaHLTFilteredEcalCandProducer',
  cands = cms.InputTag('hltEgammaCandidates'),
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
