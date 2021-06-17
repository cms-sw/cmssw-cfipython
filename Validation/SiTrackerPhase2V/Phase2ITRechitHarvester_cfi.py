import FWCore.ParameterSet.Config as cms

Phase2ITRechitHarvester = cms.EDProducer('Phase2ITRecHitHarvester',
  TopFolder = cms.string('TrackerPhase2ITRecHitV'),
  NbarrelLayers = cms.uint32(4),
  NDisk1Rings = cms.uint32(5),
  NDisk2Rings = cms.uint32(4),
  EcapDisk1Name = cms.string('EPix'),
  EcapDisk2Name = cms.string('FPix'),
  ResidualXvsEta = cms.string('Delta_X_vs_Eta'),
  ResidualXvsPhi = cms.string('Delta_X_vs_Phi'),
  ResidualYvsEta = cms.string('Delta_Y_vs_Eta'),
  ResidualYvsPhi = cms.string('Delta_Y_vs_Phi'),
  resXvseta = cms.PSet(
    name = cms.string('resolutionXFitvseta'),
    title = cms.string(';|#eta|; X-Resolution from fit [#mum]'),
    NxBins = cms.int32(41),
    xmax = cms.double(4.1),
    xmin = cms.double(0),
    switch = cms.bool(True)
  ),
  resYvseta = cms.PSet(
    name = cms.string('resolutionYFitvseta'),
    title = cms.string(';|#eta|; Y-Resolution from fit [#mum]'),
    NxBins = cms.int32(41),
    xmax = cms.double(4.1),
    xmin = cms.double(0),
    switch = cms.bool(True)
  ),
  resXvsphi = cms.PSet(
    name = cms.string('resolutionXFitvsphi'),
    title = cms.string(';#phi; X-Resolution from fit [#mum]'),
    NxBins = cms.int32(36),
    xmax = cms.double(3.1415926535897931),
    xmin = cms.double(-3.1415926535897931),
    switch = cms.bool(True)
  ),
  resYvsphi = cms.PSet(
    name = cms.string('resolutionYFitvsphi'),
    title = cms.string(';#phi; Y-Resolution from fit [#mum]'),
    NxBins = cms.int32(36),
    xmax = cms.double(3.1415926535897931),
    xmin = cms.double(-3.1415926535897931),
    switch = cms.bool(True)
  ),
  meanXvseta = cms.PSet(
    name = cms.string('meanXFitvseta'),
    title = cms.string(';|#eta|; Mean residual X from fit [#mum]'),
    NxBins = cms.int32(41),
    xmax = cms.double(4.1),
    xmin = cms.double(0),
    switch = cms.bool(True)
  ),
  meanYvseta = cms.PSet(
    name = cms.string('meanYFitvseta'),
    title = cms.string(';|#eta|; Mean residual Y from fit [#mum]'),
    NxBins = cms.int32(41),
    xmax = cms.double(4.1),
    xmin = cms.double(0),
    switch = cms.bool(True)
  ),
  meanXvsphi = cms.PSet(
    name = cms.string('meanXFitvsphi'),
    title = cms.string(';#phi; Mean residual X from fit [#mum]'),
    NxBins = cms.int32(36),
    xmax = cms.double(3.1415926535897931),
    xmin = cms.double(-3.1415926535897931),
    switch = cms.bool(True)
  ),
  meanYvsphi = cms.PSet(
    name = cms.string('meanYFitvsphi'),
    title = cms.string(';#phi; Mean residual Y from fit [#mum]'),
    NxBins = cms.int32(36),
    xmax = cms.double(3.1415926535897931),
    xmin = cms.double(-3.1415926535897931),
    switch = cms.bool(True)
  ),
  NFitThreshold = cms.uint32(100),
  mightGet = cms.optional.untracked.vstring
)
