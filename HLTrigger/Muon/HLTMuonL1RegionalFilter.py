import FWCore.ParameterSet.Config as cms

def HLTMuonL1RegionalFilter(**kwargs):
  mod = cms.EDFilter('HLTMuonL1RegionalFilter',
    saveTags = cms.bool(True),
    CandTag = cms.InputTag('hltL1extraParticles'),
    PreviousCandTag = cms.InputTag('hltL1sL1SingleMu20'),
    MinN = cms.int32(1),
    Cuts = cms.VPSet(
      cms.PSet(
        EtaRange = cms.vdouble(
          -2.5,
          -1.6
        ),
        MinPt = cms.double(20),
        QualityBits = cms.vuint32(
          6,
          7
        )
      ),
      cms.PSet(
        EtaRange = cms.vdouble(
          -1.6,
          1.6
        ),
        MinPt = cms.double(20),
        QualityBits = cms.vuint32(7)
      ),
      cms.PSet(
        EtaRange = cms.vdouble(
          1.6,
          2.5
        ),
        MinPt = cms.double(20),
        QualityBits = cms.vuint32(
          6,
          7
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
